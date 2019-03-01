<template>
	  <draggable 
	      :list="form1.templates" 
	      :component-data="getComponentData()" 
	      :options="draggableOptions">

	      <div v-for="(domain, index) in form1.templates" :key="domain.key">
	        <span class="handle">
	            <i class="el-icon-rank"></i>
	        </span>

	        <el-form-item
	          :prop="'templates.' + index + '.value1'"
	          :rules="formRules"
	          style="margin-right: 0px;"
	        >
	          <el-select v-model="domain.value1" placeholder="Select">
	            <el-option
	              v-for="item in options"
	              :key="item.value"
	              :label="item.label"
	              :value="item.value">
	            </el-option>
	          </el-select>
	        </el-form-item>

	        <el-button 
	          type="text" 
	          @click.prevent="removeDomain(domain)">
	          <i class="el-icon-delete"></i>
	        </el-button>
	        <el-button 
	          type="text" 
	          v-if="form1.templates.length-1 == index" 
	          @click="addDomain">
	            <i class="el-icon-circle-plus-outline"></i>
	        </el-button>
	      </div>
	    </draggable>
</template>


<script>

import draggable from 'vuedraggable'

export default {
	props:[
		"form1",
		"options"
	],
    components: {
        draggable,
    },
	data(){
		return {
              draggableOptions: { handle: '.handle'},
	          formRules: {
	          required: true, message: 'セクションを選択してください', 
	          trigger: 'blur'
           },
		}
	},
	methods :{
      removeDomain(item) {
        var index = this.form1.templates.indexOf(item);
        if (index !== -1) {
          this.form1.templates.splice(index, 1);
        }
      },
      addDomain() {
        this.form1.templates.push({
          key: Date.now(),
          value1: '',
          value2: 1
        });
      },
      inputChanged(value) {
        this.activeNames = value;
      },
		getComponentData(){
			return  {
				on: {
                    input: this.inputChanged
			   	},
			   	props: {
			   		value: this.activeNames
			   	}
			}
		}
	}
}
	
</script>

<style scoped>
.handle {
    cursor: grab;
}

.el-form--inline {
	margin-right: 0;
}
</style>