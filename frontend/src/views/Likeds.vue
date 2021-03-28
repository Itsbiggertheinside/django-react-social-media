<template>
    <main id='likeds'>
        <h3>Beğendiğin Gönderiler</h3>

        <div class="form-group">
            <label for="input-gorsel">Görsel</label>
            <input type="file" accept="image/*" @change="fileProcess" class="form-control-file" id="input-gorsel">
        </div>
        <div class="form-group">
            <label for="input-icerik">Açıklama</label>
            <input v-model="postData.content" type="text" class="form-control" id="input-icerik" placeholder="Açıklama">
        </div>
        <div class="form-group">
            <input @click="sendPost({post: postData})" type="button" class="btn btn-info" value="Gönder">
        </div>
    </main>
</template>

<script>
import { mapActions } from 'vuex'


export default {
    methods: {
        ...mapActions({sendPost: 'setSendPost'}),
        fileProcess(e) {
            const file = e.target.files[0]
            this.postData.image = URL.createObjectURL(file)
        }
    },
    data() {
        return {
            postData: {
                content: '',
                image: null
            },
        }
    }
}
</script>

<style>

</style>