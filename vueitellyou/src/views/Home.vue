<template>
  <el-container>
    <el-header>
      <div class="head_div_image">
        <el-image style="height: 44px; width: 136px" :src="url"></el-image>
      </div>
      <div class="my_div">
        <div
          style="padding: 0 10px"
          v-for="(item, index) in head_buttons"
          :key="index"
        >
          <el-button class="heade_button" type="text">{{
            item.name
          }}</el-button>
        </div>
      </div>
    </el-header>
    <el-container style="width: 80%">
      <el-aside width="240px">
        <el-row class="tac">
          <el-col :span="24">
            <el-menu @open="handleOpen" text-color="#fff" :unique-opened="true">
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
                    <div class="div_item">{{ item.name }}</div>
                  </el-menu-item>
                </div>
              </el-submenu>
            </el-menu>
          </el-col>
        </el-row>
      </el-aside>

      <el-main width="auto">
        <el-row>
          <el-col style="margin-botton:20px">
            <el-input placeholder="搜索关键字，空格分词 走起">
              <template slot="append">Go!</template>
            </el-input>
          </el-col>
        </el-row>
        <el-row :style="{ visibility: is_software }">
          <el-tabs
            @tab-click="fun_itellyou_language"
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
              <el-collapse accordion>
                <el-collapse-item
                  v-for="item in list_itellyou_software"
                  :key="item.id"
                >
                  <template slot="title">
                    {{ item.name }}
                    <span class="label label-primary getFileDetail"
                      >详细信息
                    </span>
                  </template>
                  <el-card class="box-card">
                    <el-row>
                      <el-col :pull="1" :span="3"><b>文件名</b> </el-col>
                      <el-col :span="15">{{ item.file_name }} </el-col>
                    </el-row>
                    <el-row>
                      <el-col :pull="1" :span="3"><b>SHA1 </b> </el-col>
                      <el-col :span="15">{{ item.my_sha1 }} </el-col>
                    </el-row>
                    <el-row>
                      <el-col :pull="1" :span="3"><b>文件大小 </b> </el-col>
                      <el-col :span="15">{{ item.file_size }} </el-col>
                    </el-row>
                    <el-row>
                      <el-col :pull="1" :span="3"><b>发布时间 </b> </el-col>
                      <el-col :span="15">{{ item.edition_date }} </el-col>
                    </el-row>
                    <el-row style="margin-top:20px">
                      <pre>{{ item.download_url }} </pre>
                    </el-row>
                    <el-row>
                      <pre>声明：本站资源均来自于官方原版，ed2k可视为P2P下载链接。由于网络环境和下载工具的不确定性，本站不保证所有人都可以下载成功，如果失败可以更换网络或者下载工具重复尝试。下载完成后务必进行SHA1校验（推荐使用<a href="https://share.weiyun.com/5gtDK6E" target="_blank">iHasher</a>），与网站核对一致后再使用。所有操作系统默认均为试用版，如有正版密钥可以有效激活，本站不提供任何激活和相关服务。请在下载完成后再考虑自愿为本站打赏或捐助，下载速度与捐助无关。如需退款请发邮件至：m@itellyou.cn，退款没有有效期，只需要提供付款截图和收款二维码即可（不是二维码名片）。<br><br><strong style="font-size:16px;">Windows 10 2004 已在<a href="https://next.itellyou.cn/Original/Index" target="_blank">next.itellyou.cn</a>更新。可使用第三方帐号直接登录，免注册。</strong></pre>
                    </el-row>
                    <el-row>
                      <div class="div_dashang">
                        <div class="div_zfb">
                          <transition name="bounce">
                            <img
                              width="129px"
                              height="150px"
                              v-show="is_pic_show"
                              src="../../src/assets/my_zfb.jpg"
                            />
                          </transition>
                        </div>
                        <div class="div_zanshang">
                          <img
                            class="my_img"
                            @click="
                              is_pic_show
                                ? (is_pic_show = false)
                                : (is_pic_show = true)
                            "
                            width="62px"
                            height="62px"
                            src="https://msdn.itellyou.cn/images/shang.png"
                          />
                        </div>
                      </div>
                    </el-row>
                  </el-card>
                </el-collapse-item>
              </el-collapse>
            </el-tab-pane>
          </el-tabs>
        </el-row>
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
        { name: "联系我", url: "", my_icon: "" }
      ],
      aside_main: {},
      list_itellyou_detail: { name: "" },
      list_itellyou_language: { name: "" },
      father_key: "",
      is_pic_show: false,
      list_itellyou_software: [],
      is_software: "hidden"
      //   file_name: "",
      //   file_size: "",
      //   my_sha1: "",
      //   key: "",
      //   name: "",
      //   download_url: "",
      //   edition_date: "",
      //   id: ""
      // }
    };
  },
  // 窗体加载时执行
  created: function() {
    this.my_window_load();
  },
  methods: {
    // 页面加载
    my_window_load() {
      this.$axios
        .get("/MyApiget_itellyou_base/")
        .then(response => {
          this.aside_main = response.data;
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
      this.list_itellyou_detail = [];

      this.$axios
        .post("/MyApiget_itellyou_detail/", qs.stringify({ fk: key }))
        .then(response => {
          this.list_itellyou_detail = response.data;
        })
        .catch(function(error) {
          console.log(error);
        })
        .then(function() {});
    },

    // 点击目录明细时触发,软件语言，软件基础信息
    itellyou_lang(key) {
      this.list_itellyou_language = [];
      //保存主键key
      this.father_key = key;
      // 获取软件多语言版本信息
      // console.log(key);
      this.$axios
        .post("/MyApiget_itellyou_lang_edition/", qs.stringify({ fk: key }))
        .then(response => {
          this.is_software = "visible";
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
    fun_itellyou_language(tab) {
      this.list_itellyou_software = [];
      this.$axios
        .post(
          "/MyApiget_itellyou_software_message/",
          qs.stringify({ fk: this.father_key, lk: tab.name })
        )
        .then(response => {
          //赋值
          response.data.forEach(element => {
            const download_url = element["download_url"];
            const list_ed2k = download_url.split("|");
            this.list_itellyou_software.push({
              file_name: list_ed2k[2],
              file_size: list_ed2k[3],
              my_sha1: list_ed2k[4],
              key: element["key"],
              name: element["name"],
              download_url: element["download_url"],
              edition_date: element["edition_date"],
              id: element["id"]
            });
          });
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
.head_div_image {
  margin-left: 118px;
}
.heade_button {
  color: #999999;
}
.heade_button:hover {
  color: white;
}
.el-col-3 {
  width: 16.66667%;
  /* align-items: end; */
  text-align: right;
}
/* .el-tabs--left,
.el-tabs--right {
  overflow: hidden;
  margin-top: 45px;
} */
/* 可以设置不同的进入和离开动画 */
/* 设置持续时间和动画函数 */
.bounce-enter-active {
  animation: bounce-in 0.5s;
}
.bounce-leave-active {
  animation: bounce-in 0.5s reverse;
}
@keyframes bounce-in {
  0% {
    transform: scale(0);
  }
  50% {
    transform: scale(1.5);
  }
  100% {
    transform: scale(1);
  }
}
.my_img {
  margin-left: -20px;
}
.div_zfb {
  /* background-color: salmon; */
  width: 50%;
  display: flex;
  justify-content: center;
  /* height: 100%; */
  /* z-index: 999999; */
}
.div_zanshang {
  width: 50%;
  height: 150px;
  display: flex;
  align-items: center;
  /* background-color: rebeccapurple; */
}
.div_dashang {
  display: flex;
  width: 100%;
}
pre {
  display: block;
  padding: 9.5px;
  margin: 0 0 10px;
  font-size: 13px;
  line-height: 1.428571429;
  color: #333;
  word-break: break-all;
  word-wrap: break-word;
  background-color: #f5f5f5;
  border: 1px solid #ccc;
  border-radius: 4px;
  white-space: pre-wrap;
  font-family: Menlo, Monaco, Consolas, "Courier New", monospace;
}

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
  background-color: #303030;
  color: #333;
  text-align: center;
  line-height: 60px;
  width: 100%;
  display: flex;
  justify-content: space-between;
  align-items: center;
}

.el-aside {
  /* background-color: #d3dce6; */
  color: #333;
}

.el-container.is-vertical {
  flex-direction: column;
  align-items: center;
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
</style>
