s<template>
　<div>	
	 <el-form-item>
      <el-button 
        type="primary" 
        round
        @click="submitForm('form1')" 
        :disabled="creatingFile.isProgress || (1 < progressValue && progressValue < 100)"
      >
        Tic Mok
      </el-button>
    </el-form-item> 
    <el-progress :percentage="progressValue" v-if="0 < progressValue && progressValue < 100"></el-progress>

      <el-table
          :data="tableData"
          style="width: 100%"
          v-if="0 < tableData.length">
          <el-table-column
            label="ファイル"
            width="180">
            <template slot-scope="scope">
              <span v-show="!scope.row.isEdit">
              <span @dblclick="enableEdit(scope.row)">{{ scope.row.name }}</span>
              <el-button type="text" @click="enableEdit(scope.row)"><i class="el-icon-edit"></i></el-button>
              </span> 
              <span v-show="scope.row.isEdit">
                <input type="text" :value="scope.row.name" @keyup.enter="onEditLabel(scope.$index, $event.target.value)" v-on:blur="onEditLabel(scope.$index, $event.target.value)">
              </span>
            </template>
          </el-table-column>
          <el-table-column
            label="操作">
            <template slot-scope="scope">
              <a :href="`/download/${scope.row.filename}`" download>
                <i class="el-icon-download"></i>
              </a>
              <el-button type="text" @click="onDeleteFile(scope.row)">
                <i class="el-icon-delete"></i>
              </el-button>
            </template>
          </el-table-column>
      </el-table>

   </div>
        
</template>

<script>
	import {v4} from 'uuid'
	import * as utils from '../../utils'

	export default {
	mounted() {
      this.loadStorage();
    },
		props:[
		       "maxFiles",
		       "form1",
		       "flag",
		       "refForm"
		       ],
		       data(){
		       	return {
		       		progressValue: 0,
		       	    creatingFile: {isProgress: false},
		       	    numbers:0,
		       	    tableData:[],
		       	    uuid: null,
		         }
		       },
		methods: {
       enableEdit(row) {
        row.isEdit = true
      },
      onEditLabel(index, value) {
        this.tableData[index].isEdit = false
        this.tableData[index].name = value
        utils.storeStorage(Vue, 'tableData', this.tableData)
      },
      onDeleteFile(row) {
        this.$confirm(`「${row.name}」を削除してもよろしいですか？`, 'Warning', {
          confirmButtonText: '削除',
          cancelButtonText: 'キャンセル',
          type: 'warning'
        }).then(() => {
        this.tableData = this.tableData.filter((e) => e.filename !== row.filename)
        this.storeStorage()

          this.$message({
            type: 'success',
            message: `「${row.name}」を削除しました`
          });

        }).catch(() => {

        });
      },
	    loadStorage() {
        const data = utils.loadStorage(Vue)
        this.numbers = data.numbers 
        this.tableData = data.tableData 
        // this.uuid = data.uuid
        this.uuid = v4()
      },
      storeStorage() {
        utils.storeStorage(Vue, 'numbers', this.numbers)
        utils.storeStorage(Vue, 'tableData', this.tableData)
        utils.storeStorage(Vue, 'uuid', this.uuid)
      },
			 updateProgress() {
          // Simulate loading
          const timer = setInterval(() => {
            this.progressValue += 1;
             if (this.progressValue >= 100) {
                // this.$refs[formName].resetFields();
               this.tableData.push(this.creatingFile)
               this.numbers += 1
               this.$message({
                   message: `ファイルを作成しました`,
                   type: 'success'
               });
               this.creatingFile = {isProgress: false}
               this.storeStorage();
               clearInterval(timer);            
             }
          }, 50);
      },
			 submitForm(formName) {
        if (this.maxFiles <= this.tableData.length) {
          this.$message({
            showClose: true,
            message: `${this.maxFiles}件以上の登録はできません`,
            type: 'warning'
          })
          return false
        }
        this.refForm().validate((valid) => {
          if (valid) {
            const templates = this.form1.templates.map((e) => {
                const key = e.value1
                return e.value1
            })
            if(this.flag.header) {
                templates.unshift('headers')
            }
            if(this.flag.footer) {
                templates.push('footers')
            }
            this.creatingFile = {isProgress: true}
            this.progressValue = 0
            this.updateProgress()
            axios.post('/api/generate', {file_numbers: this.form1.file_numbers, templates:templates, uuid: this.uuid, number: ("000" + this.numbers).slice(-3) }).then((res) => {

              const data = res.data.data
              const labelName = 'サンプル' + data.filename.substring(0,3)
                
                this.creatingFile = {
                    isProgress: false,
                    filename: data.filename, 
                    name: labelName,
                    isEdit: false
                }
                this.refForm().resetFields();
                
            }).catch((e) => {
                console.log('error')
                console.log(e)
            })

          } else {
            console.log('error submit!!');
            return false;
          }
        });
      }
    }
  }
	
</script>

<style>
	
</style>