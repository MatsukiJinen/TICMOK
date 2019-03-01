<template>	
   <div>
      <el-form-item>
          <span> 
             <el-switch
                v-model="flag.header"
                active-text="ヘッダーON"
                inactive-text="ヘッダーOFF">
              </el-switch>
          </span>
      </el-form-item>
    </div>
</template>


<script>
	export default {
		props:["flag"]
	}
</script>

<style scoped>
.non-selectable {
    padding-left: 14px;
}

.el-switch {
  padding-left: 30px; /* 変更 */
}
</style>