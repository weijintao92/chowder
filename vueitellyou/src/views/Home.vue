<template>
  <el-container>
    <el-header>
      <div>
        <el-image style="height: 44px; width: 136px" :src="url"></el-image>
      </div>
      <div class="my_div">
        <div
          style="padding: 0 10px"
          v-for="(item, index) in head_buttons"
          :key="index"
        >
          <el-button type="text">{{ item.name }}</el-button>
        </div>
        <el-dropdown>
          <span class="el-dropdown-link">
            联系我<i class="el-icon-arrow-down el-icon--right"></i>
          </span>
          <el-dropdown-menu slot="dropdown">
            <el-dropdown-item>黄金糕</el-dropdown-item>
            <el-dropdown-item>狮子头</el-dropdown-item>
            <el-dropdown-item>螺蛳粉</el-dropdown-item>
          </el-dropdown-menu>
        </el-dropdown>
      </div>
    </el-header>
    <el-container style="width: 80%">
      <el-aside width="40%">
        <el-row class="tac">
          <el-col :span="24">
            <el-menu
              default-active="2"
              class="el-menu-vertical-demo"
              @open="handleOpen"
              @close="handleClose"
              background-color="#545c64"
              text-color="#fff"
              active-text-color="#ffd04b"
              :unique-opened="true"
            >
              <el-submenu
                v-for="(item, index) in aside_main"
                :key="index"
                :index="item.key"
              >
                <template slot="title">
                  <i class="el-icon-menu"></i>
                  <span>{{ item.name }}</span>
                </template>
                <el-menu-item index="1-1">选项1</el-menu-item>
              </el-submenu>
            </el-menu>
          </el-col>
        </el-row>
      </el-aside>
      <el-container>
        <el-main>Main</el-main>
      </el-container>
    </el-container>
  </el-container>
</template>

<script>
import axios from "axios";
// import Axios from "axios";

export default {
  name: "Home",
  data() {
    return {
      url: "https://msdn.itellyou.cn/images/itellyou.cn.png",
      head_buttons: [
        { name: "站长备用", url: "", my_icon: "" },
        { name: "十年相伴", url: "", my_icon: "" },
        { name: "最新更新", url: "", my_icon: "" },
      ],
      aside_main: [],
    };
  },
  created: function () {
    //窗体加载时执行
    this.my_window_load();
  },
  methods: {
    my_window_load() {
      axios
        .get("http://180.76.98.78/get_itellyou_base/")
        .then((response) => {
          // handle success
          // console.log(response);
          this.aside_main = response.data;
          // console.log(this.my_option)
        })
        .catch(function (error) {
          // handle error
          console.log(error);
        })
        .then(function () {
          // always executed
        });
    },
    get_detail(key) {
      const formdata = new formdata();
      formdata.
      // axios(config);
      // 发送 POST 请求
      axios(
        {
        method: "post",
        url: "https://msdn.itellyou.cn/Index/GetCategory",
        data: {
          id: key
        },
        headers:{ 
          'Content-Type': 'application/x-www-form-urlencoded',
          cookie: 'UM_distinctid=175cf967505898-0b05982987527e-75143d4c-13c680-175cf9675066d9; _ga=GA1.2.319749700.1605505546; _gid=GA1.2.1136103836.1606100781; Hm_lvt_8688ca4bc18cbc647c9c68fdaef6bc24=1605692906,1605753012,1605856840,1606100781; CNZZDATA1605814=cnzz_eid%3D1910850215-1605505313-https%253A%252F%252Fwww.baidu.com%252F%26ntime%3D1606120662; _gat=1; .AspNetCore.Antiforgery.kC_Kc8he0KM=CfDJ8Jw19B-OaM1KveQHPjyyKOMX23IxH2Aa028338Aryl9Pw6dPFdQB0DniueT_xVjkR7MT5rSojIu5hG_YzZbTlvl03WuKfeEH8jDJU8aVLGKHgDCjsrnYUVSHkfX8p3gDzVPqaI6Ad5tDCkDh8WOlF5E; Hm_lpvt_8688ca4bc18cbc647c9c68fdaef6bc24=1606124045',
          'x-csrf-token': 'CfDJ8Jw19B-OaM1KveQHPjyyKOOd18a3pjYkGzjpg6yx70hqNG9_vQa70qpa-qQz2D7Eh97RRGkKZgMTkIxKiSSShMstxQsKFw5SS9vir9Rhbqah0HWI45jeBcng-Wa0IPba6xDga6ROzOfyBJAUQ3n7C9E',
        }
      }).then((response) =>{
        console.log(222222)
        console.log(response)
      })
    },
    handleOpen(key, keyPath) {
      console.log(key, keyPath);
      this.get_detail()
    },
    handleClose(key, keyPath) {
      console.log(key, keyPath);
    },
    // getabc(key, keyPath) {
    //   console.log(key, keyPath);
    // },
  },
};
</script>


<style>
.el-dropdown-link {
  cursor: pointer;
  color: #409eff;
}
.el-icon-arrow-down {
  font-size: 12px;
}
.my_div {
  display: flex;
}
.el-header {
  background-color: #b3c0d1;
  color: #333;
  text-align: center;
  line-height: 60px;
  width: 100%;
  display: flex;
  justify-content: space-between;
  align-items: center;
}

.el-aside {
  background-color: #d3dce6;
  color: #333;
  /* text-align: center; */
  /* line-height: 200px; */
}

.el-container.is-vertical {
  flex-direction: column;
  align-items: center;
}

.el-main {
  background-color: #e9eef3;
  color: #333;
  text-align: center;
  line-height: 160px;
}

body > .el-container {
  margin-bottom: 40px;
}

.el-container:nth-child(5) .el-aside,
.el-container:nth-child(6) .el-aside {
  line-height: 260px;
}
.el-image {
  position: relative;
  display: block;
  overflow: hidden;
}

.el-container:nth-child(7) .el-aside {
  line-height: 320px;
}
.el-button:hover {
  color: red;
}
</style>
