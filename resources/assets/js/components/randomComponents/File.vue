<template>
	<div>
	   <el-form 
	      :inline="true" 
	      :model="form1"  
	       label-position="left" 
	       ref="form1" 
	       class="demo-dynamic" 
	       style="max-width: 480px;">
        <el-form-item
          prop="file_numbers"
          label="ファイル数"
          :rules="[
            { required: true, message: 'ファイル数は、必須です', trigger: 'blur' },
            { type: 'number', message: 'ファイル数には、半角数字を入力してください', trigger: 'blur'}
          ]">
          <el-input-number v-model="form1.file_numbers" :min="1" :max="30" size="small"></el-input-number>
        </el-form-item>
      </el-form>
	</div>
</template>

<script>
  export default {
  	props:['form1']
  }
	
</script>

<style>
	
</style>