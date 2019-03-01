<?php

/*
|--------------------------------------------------------------------------
| Web Routes
|--------------------------------------------------------------------------
|
| Here is where you can register web routes for your application. These
| routes are loaded by the RouteServiceProvider within a group which
| contains the "web" middleware group. Now create something great!
|
*/

Auth::routes();

Route::get('/home', 'HomeController@index')->name('home');

Route::get('/', 'DownloadController@index')->name('index');

Route::get('/random', function(){
	return view('random');
});
Route::get('/manual', function(){
	return view('manual');
});

Route::get('/download/{uuid}', 'DownloadController@download')->name('home');

