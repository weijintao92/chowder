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
// import axios from "axios";
// import Axios from "axios";
import qs from 'qs';

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
      this.$axios
        .get("/get_itellyou_base/")
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

    handleOpen(key, keyPath) {
      console.log(key, keyPath);

    
      this.$axios
        .post("/get_itellyou_detail /", qs.stringify({"fk":key}) )
        .then((response) => {
          // handle success
          // console.log(response);
          console.log(response.data);
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
