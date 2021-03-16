<template>
  <div id="home">
    <h3>Hikayeler</h3>
    <div class='my-4'>
      <Stories />
    </div>
    <div class='my-4'>
      <Content />
    </div>
  </div>
</template>

<script>
import Content from '../components/home/Content.vue';
import Stories from '../components/home/Stories.vue';

export default {
  components: {
    Stories,
    Content
  }
};

</script>
