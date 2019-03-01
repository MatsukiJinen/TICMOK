<?php

namespace App\Http\Controllers;

use Illuminate\Http\Request;
use Ramsey\Uuid\Uuid;

class DownloadController extends Controller
{
    public function index(Request $request) {
		// ユーザー情報を保存する
		$uuid = $request->session()->get('uuid', Uuid::uuid4());
        $request->session()->put('uuid', $uuid);

    	return view('index', ['uuid' => $uuid]);
    }
    public function download(Request $request, $uuid)
    {
        // $uuid = '001-b7252702-d210-4536-80ec-60dbdb8e2a47';
    	$path = storage_path("app/public/{$uuid}") . '.zip';
    	return response()->download($path);
    }
}
