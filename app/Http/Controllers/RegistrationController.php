<?php

namespace App\Http\Controllers;

use Illuminate\Http\Request;
use Illuminate\Support\Facades\Hash;
use App\Http\Requests\StoreUserRequest;
use App\User;

class RegistrationController extends Controller
{
    public function register(StoreUserRequest $request)
    {
    	$user = new User();
    	$user->username = $request->username;
    	$user->password = Hash::make($request->password);
    	$user->email = $request->email;
    	$user->save();
    }
}
