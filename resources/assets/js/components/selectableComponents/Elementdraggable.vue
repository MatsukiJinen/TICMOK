
<template>
	  <draggable :list="sectionList" :component-data="getComponentData()" class="pb-3" :options="{handle:'.handle'}" v-if="0 < sectionList.length">
        <div class="" v-for="(object, i) in sectionList">
          <div class="row">
            <div>
              <div class="selectedImage selection-border" @click="enableModal(object)" :style="applyBottomStyle(sectionList, i)">
                <h2 class="title handle">{{ labels[object.key] }} (ID:{{ currentSelectoin(object).number }})</h2>
                <img class="img-responsive" :src="currentSelectoin(object).path">
                <el-button class="move-trash outline-none" type="text" @click.prevent.stop="removeDomain(object)"><i class="el-icon-delete"></i></el-button>
              </div>
            </div>
          </div>

          <el-dialog 
            title="ブロックを選択してください"
            :visible.sync="object.dialogVisible"
            width="95%">
               <div class="container">
                <div class="row" v-for="(imageArray, imageArrayIndex) in chunk(object.value)" :key="imageArrayIndex">
                  <div
                  class="image col-sm"
                  v-for="(image, imageIndex) in imageArray"
                  :key="imageIndex"
                  @click="index = imageIndex"
                  :style="blockStyle">
                   <div class="ribbon_box2" v-if="image.path">
                    <span class="ribbon13-2" v-if="image.isSelected && false" >
                      <i class="el-icon-circle-check-outline"></i>
                    </span>
                    <img @click="handleSelectedImage(object, image)" :src="image.path" :style="imageStyle">
                  </div>
                 <div v-else>
                &nbsp;
                </div>
               </div>
              </div>  
             </div>
            <span slot="footer" class="dialog-footer">
              <!-- <el-button type="primary" @click="disableModal(object)">閉じる</el-button> -->
            </span>
          </el-dialog>

        </div>
       </draggable>
</template>

<script>
  
	import draggable from 'vuedraggable'

	export default {
		props:[
		   "sectionList",
		   "labels"
		],
		components: {
          draggable
		},
		data(){
			return {
			 imageStyle: 
               { 'max-width': '100%', 'height': 'auto', border: '1px solid #dcdfe6' },
             blockStyle: 
               {'margin-bottom': '1.2rem'}
			}
		},
		methods: {
		  applyBottomStyle(object, index) {
	        if (object.length - 1 === index) {
	          return {borderBottom: '1px solid #dcdfe6'}
	        } else {
	          return {borderBottom: 'none'}
	        }
	      },
      currentSelectoin(object) {
        const o = object.value.find((e) => {
          return e.isSelected
        })
        if(!o) {
          console.log('undefined', object)
          const chance = new Chance()
          const index = chance.integer({min:0, max:object.value.length - 1})
          object.value = object.value.map((e, i) => {
            e.isSelected = (i === index)
            return e;
          });
          return object.value[index]
        }

        return o;
      },
      handleSelectedImage(object, image) {
        object.value.forEach((e) => {
          e.isSelected = (e.path === image.path)
        })
        this.disableModal(object)
      },
       disableModal(object) {
        object.dialogVisible = false
      },
	      enableModal(object) {
	        object.dialogVisible = true
	      },
      chunk(array) {
        return _.chunk(array, 3).map((e) => {
        if(e.length === 3) {
          return e
        }
        const remains = []
        for(let i = 0; i < 3 - e.length; i++) {
          remains.push('')
        }
        return _.concat(e, remains)
      })
      },
	      removeDomain(object) {
　　　　　const title = this.labels[object.key]
        const current = this.currentSelectoin(object)
        const h = this.$createElement;
        this.$msgbox({
          title: 'Delete',
          message: h('p', null, [
            h('span', null, `「${title}(ID:${current.number})」を削除してもよろしいですか？`),
            h('i', { style: 'color: teal' }, '')
          ]),
          showCancelButton: true,
          confirmButtonText: 'OK',
          type:'warning',
          cancelButtonText: 'Cancel',
          beforeClose: (action, instance, done) => {
            if (action === 'confirm') {
              instance.confirmButtonLoading = true;
              instance.confirmButtonText = 'Loading...';
              setTimeout(() => {
                done();
                setTimeout(() => {
                  instance.confirmButtonLoading = false;
                }, 300);
              }, 3000);
            } else {
              done();
            }
          }
        }).then(action => {
          var index = this.sectionList.indexOf(object);
          if (index !== -1) {
            this.sectionList.splice(index, 1);
          }
          this.$message({
            type: 'success',
            message: `「${title}(ID:${current.number})」を削除しました`
          });
        });

      },
    inputChanged(value) {
      this.activeNames = value;
    },
    getComponentData() {
      return {
      on: {
        input: this.inputChanged
      },
      props: {
        value: this.activeNames
      }
   };
  }
 }
}
</script>

<style scoped>

  @keyframes RightToLeft {
  0% {
    opacity: 1;
    transform: translateX(500px);
  }
  100% {
    opacity: 1;
    transform: translateX(0);
  }
}

.selectedImage {
  animation-duration: 0.2s;
  animation-name: RightToLeft;
}

</style>
