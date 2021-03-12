<template>
  <div class="home">
    <b-container fluid>
      <b-row>
        <b-col sm='0' md='4'>
          <LeftMenu />
        </b-col>
        <b-col>
          <h1>Content</h1>
        </b-col>
        <b-col sm='0' md='4'>
          <RightMenu />
        </b-col>
      </b-row>
    </b-container>
  </div>
</template>

<script>
import LeftMenu from '../components/home/LeftMenu';
import LeftMenu from '../components/home/RightMenu';

export default {
  components: {
    LeftMenu, RightMenu
  }
};

</script>
