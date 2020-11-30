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

        <span class="el-dropdown-link">
          联系我<i class="el-icon-arrow-down el-icon--right"></i>
        </span>
      </div>
    </el-header>
    <el-container style="width: 80%">
      <el-aside width="240px">
        <el-row class="tac">
          <el-col :span="24">
            <el-menu
              @open="handleOpen"
              @close="handleClose"
              text-color="#fff"
              :unique-opened="true"
            >
              <el-submenu
                v-for="(item, index) in aside_main"
                :key="index"
                :index="item.key"
              >
                <template slot="title">
                  <div class="div_my_link">
                    <a>{{ item.name }}</a>
                  </div>
                </template>

                <div class="div_list_itellyou_detail">
                  <el-menu-item
                    v-for="(item, index) in list_itellyou_detail"
                    :key="index"
                    :index="item.key"
                    @click="itellyou_lang(item.key)"
                  >
                    <!-- v-bind:style="{'background-color':my_background_color} -->
                    <div class="div_item">{{ item.name }}</div>
                  </el-menu-item>
                </div>
              </el-submenu>
            </el-menu>
          </el-col>
        </el-row>
      </el-aside>

      <el-main width="auto">
        <el-tabs
          @tab-click="itellyou_software"
          type="border-card"
          tab-position="left"
          style="height: auto;"
        >
          <el-tab-pane
            v-for="item in list_itellyou_language"
            :label="item.lang"
            :key="item.key"
            :name="item.key"
          >
            <div
              class="checkbox"
              v-for="item in list_itellyou_software"
              :key="item.key"
            >
              <el-checkbox>
                {{ item.name }}
                <!-- <el-button type="primary" size="mini">主要按钮</el-button> -->
                <span
                  class="label label-primary getFileDetail"
                  data-loaded="false"
                  data-id="3fbb85c2-6445-496f-af4d-31fab85755a0"
                  >详细信息
                </span>
              </el-checkbox>
              <div style="width:500px;height:500px; background-color: #3c85c4;">
                nihao
              </div>
            </div>
          </el-tab-pane>
        </el-tabs>
      </el-main>
    </el-container>
  </el-container>
</template>

<script>
// import axios from "axios";
// import Axios from "axios";
import qs from "qs";

export default {
  name: "Home",
  data() {
    return {
      url: "https://msdn.itellyou.cn/images/itellyou.cn.png",
      head_buttons: [
        { name: "站长备用", url: "", my_icon: "" },
        { name: "十年相伴", url: "", my_icon: "" },
        { name: "最新更新", url: "", my_icon: "" }
      ],
      aside_main: [],
      list_itellyou_detail: [],
      list_itellyou_language: [],
      list_itellyou_software: [],
      father_key: ""
    };
  },
  created: function() {
    // 窗体加载时执行
    this.my_window_load();
  },
  methods: {
    my_window_load() {
      this.$axios
        .get("/get_itellyou_base/")
        .then(response => {
          // handle success
          // console.log(response);
          this.aside_main = response.data;
          // console.log(this.my_option)
        })
        .catch(function(error) {
          // handle error
          console.log(error);
        })
        .then(function() {
          // always executed
        });
    },
    // 打开
    handleOpen(key) {
      // console.log(key);
      this.$axios
        .post("/get_itellyou_detail/", qs.stringify({ fk: key }))
        .then(response => {
          // handle success
          // console.log(response);
          // console.log(response.data);
          this.list_itellyou_detail = response.data;
          // console.log(this.my_option)
        })
        .catch(function(error) {
          // handle error
          console.log(error);
        })
        .then(function() {
          // always executed
        });
    },
    // 关闭
    handleClose() {
      // console.log(key, keyPath);
    },
    // 点击目录明细时触发,软件语言，软件基础信息
    itellyou_lang(key) {
      //保存主键key
      this.father_key = key;
      // 获取软件多语言版本信息
      // console.log(key);
      this.$axios
        .post("/get_itellyou_lang_edition/", qs.stringify({ fk: key }))
        .then(response => {
          //赋值
          this.list_itellyou_language = response.data;
        })
        .catch(function(error) {
          console.log(error);
        })
        .then(function() {
          // always executed
        });
    },
    itellyou_software(tab) {
      console.log(tab.name);
      this.$axios
        .post(
          "/get_itellyou_software_message/",
          qs.stringify({ fk: this.father_key, lk: tab.name })
        )
        .then(response => {
          console.log(response.data);
          //赋值
          this.list_itellyou_software = response.data;
        })
        .catch(function(error) {
          console.log(error);
        })
        .then(function() {
          // always executed
        });
    }
  }
};
</script>

<style>
.checkbox {
  display: block;
  min-height: 20px;
  padding-left: 20px;
  margin-top: 10px;
  margin-bottom: 10px;
  /* vertical-align: middle; */
}
.label {
  display: inline;
  padding: 0.2em 0.6em 0.3em;
  font-size: 75%;
  font-weight: bold;
  line-height: 1;
  color: #fff;
  text-align: center;
  white-space: nowrap;
  vertical-align: baseline;
  border-radius: 0.25em;
}
.label-primary {
  background-color: #428bca;
}
.getFileDetail {
  cursor: pointer;
}
.tabs-left > .nav-tabs {
  top: auto;
  margin-bottom: 0;
  border-color: #c5d0dc;
  float: left;
}

.nav-tabs {
  border-color: #c5d0dc;
  margin-bottom: 0;
  margin-left: 0;
  position: relative;
  top: 1px;
}
.nav-tabs {
  border-bottom: 1px solid #ddd;
}
.nav {
  padding-left: 0;
  margin-bottom: 0;
  list-style: none;
}
ul,
ol {
  margin-top: 0;
  margin-bottom: 10px;
}
*,
*:before,
*:after {
  -webkit-box-sizing: border-box;
  -moz-box-sizing: border-box;
  box-sizing: border-box;
}

ul {
  display: block;
  list-style-type: disc;
  margin-block-start: 1em;
  margin-block-end: 1em;
  margin-inline-start: 0px;
  margin-inline-end: 0px;
  padding-inline-start: 40px;
}
a:hover {
  text-decoration: underline;
}
/* .div_my_link {
  display: flex;
} */
/* .el-link {
  color: #fff !important;
} */

.el-submenu {
  list-style: none;
  margin: 2px;
  padding-left: 0;
  background-color: #3c85c4;
}
.el-submenu__title:hover {
  background-color: #3c85c4;
}
.el-submenu__title {
  line-height: 0px !important;
  height: 30px;
  display: flex;
  align-items: center;
}

.div_list_itellyou_detail {
  max-height: 300px;
  border: 1px solid #3c85c4;
  /* 设置滚动条 */
  overflow-y: auto;
  overflow-x: hidden;
}
.el-menu-item {
  /* background-color: white !important; */
  color: black !important;
  padding-left: 10px !important;
  height: 20px !important;
  height: 50px;
  line-height: 18px !important;
  padding: 0 45px;
  min-width: 200px;
}
/* .div_item{
  border: 1px solid yellow;
  width: 197px;
} */
.el-menu-item:focus div {
  background-color: #3c85c4;
}

.el-submenu__icon-arrow {
  position: absolute;
  top: 50%;
  right: 20px;
  margin-top: -7px;
  transition: transform 0.3s;
  font-size: 12px;
  visibility: hidden;
}

.el-dropdown-link {
  cursor: pointer;
  color: #409eff;
}
.el-icon-arrow-down {
  font-size: 12px;
}
/* 头部 */
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
}

.el-container.is-vertical {
  flex-direction: column;
  align-items: center;
}

.el-main {
  /* background-color: #e9eef3; */
  /* color: #333; */
  /* text-align: center; */
  /* line-height: 160px; */
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
