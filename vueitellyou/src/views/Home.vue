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
        </el-dropdown>
      </div>
    </el-header>
    <el-container style="width: 80%">
      <el-aside width="40%">
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
                  <!-- <i class="el-icon-menu"></i> -->
                  <span>{{ item.name }}</span>
                </template>



                <!-- 目录明细 -->
                <div class="div_list_itellyou_detail">
                  <el-menu-item
                    v-for="(item, index) in list_itellyou_detail"
                    :index="index"
                    :key="item.id"
                    @click="itellyou_final(item.key)"
                    >{{ item.name }}</el-menu-item
                  >
                </div>
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
    handleOpen(key, keyPath) {
      console.log(key, keyPath);
      this.$axios
        .post("/get_itellyou_detail/", qs.stringify({ fk: key }))
        .then((response) => {
          // handle success
          // console.log(response);
          console.log(response.data);
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
    handleClose(key, keyPath) {
      console.log(key, keyPath);
    },
    //点击目录明细时触发
    itellyou_final(key){
      console.log(key)
      
    }
    // getabc(key, keyPath) {
    //   console.log(key, keyPath);
    // },
  },
};
</script>


<style>
.el-submenu {
  list-style: none;
  margin: 2px;
  padding-left: 0;
  background-color: #3c85c4;
}
.div_list_itellyou_detail {
  max-height: 579px;

  border: 1px solid #3c85c4;
  /* 设置滚动条 */
  overflow-y: auto;
  overflow-x: hidden;

  /* margin-bottom: 2px; */
}
.el-menu-item {
  background-color: white !important;
  color: black !important;
  padding-left: 10px !important;
  height: 25px!important;
}

.el-submenu .el-menu-item {
    height: 50px;
    line-height: 31px!important;
    padding: 0 45px;
    min-width: 200px;
}
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
