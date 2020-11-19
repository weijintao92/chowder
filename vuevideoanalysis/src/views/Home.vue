<template>
  <!-- <div id="app"> -->
  <el-container>
    <el-header
      ><h1>格调vip解析</h1>
      <h4>
        免责声明：本站所有视频资源均来自网络。服务器仅展示第三方网站接口页面，并不存储任何视频资源。因此经由本站搜索所产生
        的任何结果皆不代表本站立场，本站不对其真实合法性以及版权负责，亦不承担任何法律责任。
      </h4></el-header
    >
    <el-main>
      <el-row>
        <el-col :span="4">
          <el-select v-model="my_analysis" placeholder="请选择">
            <el-option
              v-for="(item, index) in my_option"
              :key="index"
              :label="'解析线路' + (index + 1)"
              :value="item"
            >
            </el-option>
          </el-select>
        </el-col>
        <el-col :span="19" style="margin-left: 30px">
          <el-input
            v-model="my_url"
            ref="my_input_url"
            placeholder="电脑使用Ctrl+V粘贴网址-手机直接长按粘贴网址"
          />
        </el-col>
      </el-row>

      <div style="margin-top: 5px; border: 1px solid yellow">
        <el-button type="primary" @click="begin_analysis">Go-开始解析</el-button
        ><el-button type="primary" @click="begin_analysis_full"
          >Go-全屏解析</el-button
        >
      </div>
      <div style="border: 1px solid red; margin-top: 2px;height100%">
        <iframe
          id="google_esf"
          name=" google_esf"
          :src="my_iframe_src"
          marginheight="0"
          marginwidth="0"
          frameborder="0"
          width="100%"
          height="100%"
          scrolling="no"
          allowfullscreen="true"
          allowtransparency="true"
        ></iframe>
      </div>
    </el-main>
    <el-footer>
      <h4>
        仅供学习和交流使用！如有侵权请邮件1109765190@qq.com<br />请勿相信视频中的广告及其他信息！
      </h4></el-footer
    >
  </el-container>
  <!-- <router-view /> -->
  <!-- </div> -->
</template>


<script>
import axios from "axios";

export default {
  name: "Home",
  data() {
    return {
      my_option: [],
      my_analysis: "",
      my_url: "",
      my_iframe_src: "http://jqaaa.com/jx.php?url=",
    };
  },
  created: function () {
    //窗体加载时执行
    this.my_window_load();
  },
  methods: {
    jump() {
      this.$router.push("/About");
    },

    //窗体加载，基础的加载
    my_window_load() {
      axios
        .get("http://180.76.98.78/snippets/?format=json")
        .then((response) => {
          // handle success
          // console.log(response);
          this.my_option = response.data;
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
    //开始解析
    begin_analysis() {
      if (!this.my_url) {
        this.$message({
          showClose: true,
          message: "请输入您需要解析的地址！",
          type: "warning",
        });
        // this.$refs['my_input_url'].focus()
        this.$refs.my_input_url.focus();
        return false;
      }

      this.my_iframe_src = this.my_analysis + this.my_url;
      // console.log(this.my_iframe_src);
    },
    begin_analysis_full() {
      if (!this.my_url) {
        this.$message({
          showClose: true,
          message: "请输入您需要解析的地址！",
          type: "warning",
        });
        this.$refs["my_input_url"].focus();
        return false;
      }
      window.open(this.my_analysis + this.my_url);
    },
  },
};
</script>
<style>
.el-container{
position: absolute;
height: 98.5%;
width: 99%;
}
.el-col {
  margin-left: -5px !important;
}
.el-header,
.el-footer {
  background-color: #b3c0d1;
  color: #333;
  text-align: center;
  height: 20% !important;
}

.el-main {
  background-color: #e9eef3;
  color: #333;
  text-align: center;
  height: 60% !important;
}
</style>