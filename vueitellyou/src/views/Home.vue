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
                    @click="itellyou_final(item.key)"
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
        <div>
          <el-input
            size="small"
            placeholder="搜索关键字，空格分词 走起"
            v-model="input2"
          >
            <template size="small" slot="append">Go!</template>
          </el-input>
        </div>

        <div>
          <div class="col-md-9" role="main">
            <form id="search_form" style="margin-bottom: 8px; margin-top: 2px">
              <div class="input-group">
                <input
                  class="form-control"
                  name="keyword"
                  placeholder="搜索关键字，空格分词 走起"
                /><span class="input-group-btn"
                  ><button class="btn btn-default">Go!</button></span
                >
              </div>
            </form>
            <div class="bs-docs-section">
              <div class="row">
                <div class="col-md-12">
                  <div
                    class="tabbable tabs-left"
                    id="view_data_container"
                    style="max-height: 849px; overflow: auto"
                  >
                    <ul class="nav nav-tabs">
                      <li class="active">
                        <a
                          href="#lang_041dbbd2-c198-4523-b438-590128265d82"
                          data-loadproduct="true"
                          data-loaded="true"
                          data-id="041dbbd2-c198-4523-b438-590128265d82"
                          data-toggle="tab"
                          data-loading="false"
                          >中文 - 简体</a
                        >
                      </li>
                      <li>
                        <a
                          href="#lang_e15db4de-c094-4c50-822a-98ad50daba4f"
                          data-loadproduct="true"
                          data-loaded="false"
                          data-id="e15db4de-c094-4c50-822a-98ad50daba4f"
                          data-toggle="tab"
                          >英语</a
                        >
                      </li>
                      <li>
                        <a href="#select_data_box" data-toggle="tab"
                          >已勾选(<span>0</span>)</a
                        >
                      </li>
                    </ul>
                    <div class="tab-content">
                      <div
                        class="tab-pane active"
                        id="lang_041dbbd2-c198-4523-b438-590128265d82"
                      >
                        <ul class="list-unstyled">
                          <li>
                            <div class="checkbox">
                              <label
                                ><input
                                  type="checkbox"
                                  data-url="ed2k://|file|cn_disc_1_windows_small_business_server_2008_standard_and_premium_installation_x64_dvd_x14-76588.iso|3926978560|91A07264117D4E4C24EF4A209E496FD2|/"
                                  value="bb8af02d-c34a-4207-99a2-3200711fd0cc"
                                />Disc 1: Windows Small Business Server 2008
                                Standard and Premium Installation (x64) - DVD
                                (Chinese - Simplified)</label
                              >
                              <span
                                class="label label-primary getFileDetail"
                                data-loaded="false"
                                data-id="bb8af02d-c34a-4207-99a2-3200711fd0cc"
                                >详细信息</span
                              >
                            </div>
                          </li>
                          <li>
                            <div class="checkbox">
                              <label
                                ><input
                                  type="checkbox"
                                  data-url="ed2k://|file|cn_disc_2_component_technologies_for_server_repair_x64_x14-76591.iso|2184601600|6A9DF8733401F16DB2B95C02CE5BD8C2|/"
                                  value="6257421e-2605-4734-a86b-f5ae6110c0e0"
                                />Disc 2: Component Technologies for Server
                                Repair (x64) - DVD (Chinese-Simplified)</label
                              >
                              <span
                                class="label label-primary getFileDetail"
                                data-loaded="false"
                                data-id="6257421e-2605-4734-a86b-f5ae6110c0e0"
                                >详细信息</span
                              >
                            </div>
                          </li>
                        </ul>
                      </div>
                      <div
                        class="tab-pane"
                        id="lang_e15db4de-c094-4c50-822a-98ad50daba4f"
                      ></div>
                      <div class="tab-pane" id="select_data_box">
                        <pre>声明：本站资源均来自于官方原版，ed2k可视为P2P下载链接。由于网络环境和下载工具的不确定性，本站不保证所有人都可以下载成功，如果失败可以更换网络或者下载工具重复尝试。下载完成后务必进行SHA1校验（推荐使用<a href="https://share.weiyun.com/5gtDK6E" target="_blank">iHasher</a>），与网站核对一致后再使用。所有操作系统默认均为试用版，如有正版密钥可以有效激活，本站不提供任何激活和相关服务。请在下载完成后再考虑自愿为本站打赏或捐助，下载速度与捐助无关。如需退款请发邮件至：m@itellyou.cn，退款没有有效期，只需要提供付款截图和收款二维码即可（不是二维码名片）。<br><br><strong style="font-size:16px;">Windows 10 2004 已在<a href="https://next.itellyou.cn/Original/Index" target="_blank">next.itellyou.cn</a>更新。可使用第三方帐号可以直接登录，免注册。</strong></pre>
                      </div>
                    </div>
                  </div>
                </div>
              </div>
            </div>
          </div>
        </div>
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
        { name: "最新更新", url: "", my_icon: "" },
      ],
      aside_main: [],
      list_itellyou_detail: [],
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
    // 打开
    handleOpen(key) {
      // console.log(key);
      this.$axios
        .post("/get_itellyou_detail/", qs.stringify({ fk: key }))
        .then((response) => {
          // handle success
          // console.log(response);
          // console.log(response.data);
          this.list_itellyou_detail = response.data;
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
    // 关闭
    handleClose() {
      // console.log(key, keyPath);
    },
    //点击目录明细时触发
    itellyou_final(key) {
      this.my_background_color = "#3c85c4";
      //获取软件多语言版本信息
      // console.log(key);
      this.$axios
        .post("/get_itellyou_lang_edition/", qs.stringify({ fk: key }))
        .then((response) => {
          // handle success
          console.log(response);
          // console.log(response.data);
          // this.list_itellyou_detail = response.data;
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
    // getabc(key, keyPath) {
    //   console.log(key, keyPath);
    // },
  },
};
</script>


<style>
.tabs-left>.nav-tabs {
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
ul, ol {
    margin-top: 0;
    margin-bottom: 10px;
}
*, *:before, *:after {
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
A:hover {
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
