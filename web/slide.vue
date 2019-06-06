<template>
  <div class="page">
    <section v-if="idx < 0">
      <p class="label">{{user.title}}</p>
      <p class="label">{{user.author}}</p>
      <p class="label">{{user.date}}</p>
    </section>
    <section v-else>{{slide[idx]}}</section>
  </div>
</template>

<script>
export default {
  data() {
    return {
      idx: -1,
      user: {
        title: "这里是名字",
        author: "simdd",
        date: "2019/02/10"
      },
      slide: ["page1", "page2"]
    };
  },

  mounted() {
    console.log(1);
    document.addEventListener("keydown", e => {
      if (e.keyCode === 32) {
        if (this.idx >= this.slide.length - 1) {
          this.idx = -1;
        } else {
          this.idx = this.idx + 1;
        }
      }
    });
  }
};
</script>

<style>
* {
  padding: 0;
  margin: 0;
}
</style>

<style lang="less" scoped>
.page {
  width: 100vw;
  height: 100vh;
  display: flex;
  justify-content: center;
  align-items: center;

  .label {
    padding-top: 20px;
    padding-bottom: 20px;
  }
}
</style>
