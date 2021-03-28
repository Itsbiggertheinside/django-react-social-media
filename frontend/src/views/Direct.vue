<template>
  <div id="direct">
    <b-row>
        <b-col md="3">
            <b-nav vertical>
                <b-nav-item v-for="followed in followingList[0].followeds" :key="followed.id">
                    <b-avatar class="mr-3 align-top" variant="light" :src="followed.picture" size="1.8rem"></b-avatar>
                    <span>{{followed.username}}</span>
                </b-nav-item>
            </b-nav>
        </b-col>
        <b-col md="9">
            <b-row>
                <b-col sm="12">
                    <b-card border="dark">
                        <b-card-body>
                            <b-row>
                                <b-col sm="12">
                                    <span>Lorem ipsum dolor sit amet consectetur adipisicing elit. Dolorum,</span>
                                </b-col>
                                <b-col sm="12" align="right">
                                    <span>Lorem ipsum dolor sit amet consectetur adipisicing elit. Dolorum,</span>
                                </b-col>
                                <b-col sm="12">
                                    <span>Lorem ipsum dolor sit amet consectetur adipisicing elit. Dolorum,</span>
                                </b-col>
                                <b-col sm="12">
                                    <span>Lorem ipsum dolor sit amet consectetur adipisicing elit. Dolorum,</span>
                                </b-col>
                                <b-col sm="12" align="right">
                                    <span>Lorem ipsum dolor sit amet consectetur adipisicing elit. Dolorum,</span>
                                </b-col>
                                <b-col sm="12">
                                    <span>Lorem ipsum dolor sit amet consectetur adipisicing elit. Dolorum,</span>
                                </b-col>
                            </b-row>
                        </b-card-body>
                    </b-card>
                </b-col>
                <b-col sm="12">
                    <b-input-group>
                        <b-form-input type="text" placeholder="Mesajınız"></b-form-input>

                        <b-input-group-append>
                            <b-button variant="outline-primary">Gönder</b-button>
                        </b-input-group-append>
                </b-input-group>
                </b-col>
            </b-row>
        </b-col>
    </b-row>
  </div>
</template>

<script>
import { mapGetters } from 'vuex'


export default {
    data() {
        return {
            
        }
    },
    computed: {
      ...mapGetters({followingList: 'getFollowingList'})
    },
    mounted() {
        
    }
}
</script>

<style>

</style>