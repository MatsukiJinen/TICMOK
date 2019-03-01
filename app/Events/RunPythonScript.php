<?php

namespace App\Events;

use Illuminate\Broadcasting\Channel;
use Illuminate\Queue\SerializesModels;
use Illuminate\Broadcasting\PrivateChannel;
use Illuminate\Broadcasting\PresenceChannel;
use Illuminate\Foundation\Events\Dispatchable;
use Illuminate\Broadcasting\InteractsWithSockets;
use Illuminate\Contracts\Broadcasting\ShouldBroadcast;

use Symfony\Component\Process\Process;
use Symfony\Component\Process\Exception\ProcessFailedException;

class RunPythonScript implements ShouldBroadcast
{
    use Dispatchable, InteractsWithSockets, SerializesModels;

    public $script_name;
    public $data;
    /**
     * Create a new event instance.
     *
     * @return void
     */
    public function __construct($script_name, $data)
    {
        $this->script_name = $script_name;
        $this->data = $data;
    }

    public function run()
    {
        $data = $this->data;

        $params = json_encode($data);
        $root_path = base_path();
        $script_name = $this->script_name;
        $script_path = "{$root_path}/scripts/{$script_name}";

            $process = new Process("python3 ${script_path} '{$params}'");
            // $process->setTimeout(3600);
            $process->setTimeout(50);
            $process->start();

            $process->wait(function ($type, $buffer) {
                if (Process::ERR === $type) {
                    echo 'ERR > '.$buffer;
                } else {
                    echo 'OUT > '.$buffer;
                }
            });

            // executes after the command finishes
            if (!$process->isSuccessful()) {
                throw new ProcessFailedException($process);
            }

            echo $process->getOutput();



    }
    /**
     * Get the channels the event should broadcast on.
     *
     * @return \Illuminate\Broadcasting\Channel|array
     */
    public function broadcastOn()
    {
        // return new Channel('test_channel');
        logger('broadcastOn-1234');
        // $this->data['x_soket_id']
        return new PrivateChannel('order.' . $this->data['uuid']);
    }

    // public function broadcastWith()
    // {
    //     return [ 'id' => $this->user['id'],
    //         'name' => $this->user['name'],
    //         'email' => $this->user['email']
    //     ];
    // }

    // JavaScript側で受け取る時は、名前の先頭に「.」を付加する
    // window.Echo.channel("test_channel").listen(".test_event", e => {
    // https://laravel.com/docs/5.6/broadcasting
    public function broadcastAs()
    {
        return 'test_event';
    }
}
