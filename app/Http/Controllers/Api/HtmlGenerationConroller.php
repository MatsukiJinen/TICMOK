<?php

namespace App\Http\Controllers\Api;

use Illuminate\Http\Request;
use App\Http\Controllers\Controller;
use App\Events\RunPythonScript;
use Illuminate\Support\Facades\Auth;
use Ramsey\Uuid\Uuid;

class HtmlGenerationConroller extends Controller
{
    public function generate2(Request $request) {
    	// $data = $request->input('data');

		$templates = $request->input('templates');
		$uuid4 = $request->input('uuid');
		$number = '001';

	    $data = [
	     	'templates' => $templates,
	     	// 'uuid' => $uuid4->toString()
	     	'uuid' =>  $uuid4,
	     	'filename' => $number . "-" .$uuid4
     	];

		event(new RunPythonScript('run3.py', $data));
		return response()->json(['templates' => $templates, 'data' => $data]);
    }

    public function generate(Request $request) {
		$file_numbers = $request->input('file_numbers');
		$templates = $request->input('templates');
		$uuid4 = $request->input('uuid');
		$number = $request->input('number');
		// $x_soket_id = $request->header('X-Socket-ID');

		// i.e. 25769c6c-d34d-4bfe-ba98-e0ee856f3e7a
		// $uuid4 = Uuid::uuid4();

	     $data = [
	     	'numbers' => $file_numbers,
	     	'templates' => $templates,
	     	// 'uuid' => $uuid4->toString()
	     	'uuid' =>  $uuid4,
	     	'filename' => $number . "-" .$uuid4
     	];

		event(new RunPythonScript('run.py', $data));
		return response()->json(['result' => $file_numbers, 'templates' => $templates, 'data' => $data]);
    }
}
