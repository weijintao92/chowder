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
      var fd = new FormData();
      fd.append("id", key); //后台给的类型（4个）
      // var config = { headers: { "Content-Type": "multipart/form-data" } };

      // axios(config);
      // console.log(key)
      // const params = new URLSearchParams();
      // params.append("id",key)
      // 发送 POST 请求
      axios({
        method: "post",
        // url: "https://msdn.itellyou.cn/Index/GetCategory",
        url: "https://msdn.itellyou.cn/Index/GetCategory",
        fd,

        headers: {
          "content-type": "application/x-www-form-urlencoded; charset=UTF-8",
          "xsrfCookieName":"UM_distinctid=175ea4b3dea63-0cec85404da311-6f5b7628-1fa400-175ea4b3deb9f1; _ga=GA1.2.1819646167.1605953601; never_show_donate_auto=true; CNZZDATA1605814=cnzz_eid%3D349703014-1605951993-https%253A%252F%252Fwww.baidu.com%252F%26ntime%3D1606138593; Hm_lvt_8688ca4bc18cbc647c9c68fdaef6bc24=1605953601,1606044268,1606138809; _gid=GA1.2.794892782.1606138809; .AspNetCore.Antiforgery.kC_Kc8he0KM=CfDJ8Jw19B-OaM1KveQHPjyyKOMilfzCVKOCa3wxqXt2cA3jg9TAPpA5Fyna-dNipm1VSXQ5LKCy7QPtcJ9DASbk0KXNALze7BkIq02mT97GbmSPwwJy6TByDHCwT-iTmhhVkZodDpyiP5QbM4PLn3pkM2k; _gat=1; Hm_lpvt_8688ca4bc18cbc647c9c68fdaef6bc24=1606140996",
          "x-csrf-token":"CfDJ8Jw19B-OaM1KveQHPjyyKOOd18a3pjYkGzjpg6yx70hqNG9_vQa70qpa-qQz2D7Eh97RRGkKZgMTkIxKiSSShMstxQsKFw5SS9vir9Rhbqah0HWI45jeBcng-Wa0IPba6xDga6ROzOfyBJAUQ3n7C9E",
          
          "accept": "*/*",
          "accept-encoding": "gzip, deflate, br",
          "accept-language": "zh-CN,zh;q=0.9",
          "content-length": "39",
          "origin": "https://msdn.itellyou.cn",
          "referer": "https://msdn.itellyou.cn/",
          "sec-fetch-dest": "empty",
          "sec-fetch-mode": "cors",
          "sec-fetch-site": "same-origin",
          "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4315.4 Safari/537.36",
          "x-requested-with": "XMLHttpRequest",

        },
      }).then((response) => {
        console.log(222222);
        console.log(response);
      });
    },
    handleOpen(key, keyPath) {
      console.log(key, keyPath);
      console.log(key);
      this.get_detail(key);
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
