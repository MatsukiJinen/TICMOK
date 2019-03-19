<template>
<el-row class="tac">
  <el-col>
    <el-menu
      class="el-menu-vertical-demo"
      background-color="#fff"
      text-color="#000"
      active-text-color="#000">
      <img src="../../../../img/Tic Moklogo.png" alt="">
      <el-menu-item index="index"  v-for="(item,index) in options" 
      :key="item.value" 
      @click="handelChange({
          value: item.value,
          label: item.label
          })">
        <span>{{ item.label }}</span>
      </el-menu-item>
    </el-menu>
  </el-col>
</el-row>
</template>

<script>
  
export default {
  props:["options","allList","sectionList"],
  data(){
    return {
  　　　currentValue: {
          value: 'contents',
          label: 'コンテンツ'
          },
    }
  },
  methods: {
   handelChange(currentValue) {

        // this.$notify({
        //       title: '追加',
        //       message: `アイテムを追加しました`,
        //       type: 'success'
        //     });

       this.currentValue = currentValue

        const key = this.currentValue.value
        console.log('key',key)
        const value = this.allList[key]

        this.sectionList.push({ 
          dialogVisible: false,
          key: key, 
          value: _.fill(Array(value), 0).map((_, index) => {
          const number = ('000' + (index)).slice(-3)
          const pngName  = ('000' + index).slice(-3)
          const chance = new Chance()
          const selectedIndex = chance.integer({min:0, max:value - 1})
          const isSelected = (index === selectedIndex) ? true : false;
          return {isSelected: isSelected, number: number, path: `/img/${key}/${pngName}.png`}
        })})

        console.log('sectionList', this.sectionList)

      },
   }
} 

</script>

<style scoped>

li {
  text-align: center;
   border-bottom: 2px solid #00000038;
   width: 80%;
   margin: 0 auto;
   height: 80px;
}

img {
  padding-top: 30px;
}

span {
  padding-bottom: 10px;
}


</style>