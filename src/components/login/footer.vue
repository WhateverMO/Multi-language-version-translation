<template>
  <div>
    <div class="footer">
      <ul>
        <li>计算机科学与工程学院</li>
        <li>
          本站所收录的作品、社区话题、用户评论、用户上传内容或图片等均属用户个人行为。如前述内容侵害您的权益，欢迎举报投诉，一经核实，立即删除，本站不承担任何责任
        </li>
      </ul>
    </div>
  </div>
</template>

<script>
export default {
  name: "foot",
};
</script>

<style>
.footer {
  height: 2vh;
  margin-top: 8vh;
  text-align: center;
  position: sticky;
  bottom: 0;
}
.footer li {
  font-size: small;
}
li {
  list-style: none;
}
</style>