<template>
    <div id="comments">
        <b-list-group>
            <b-list-group-item v-for="comment in comments" :key="comment.id" class="flex-column align-items-start">
                <div class="d-flex w-100 justify-content-between">
                    <div class="mb-3">
                        <b-avatar :src="comment.profile_picture" size="1.5rem"></b-avatar>
                        <span class="ml-2 profile-username">{{comment.username}}</span>
                    </div>
                    <small class="text-muted">{{comment.created_at}} önce</small>
                </div>

                <p class="mb-1">{{comment.content}}</p>

                <small class="text-muted">Beğen | Yorum Yap</small>
            </b-list-group-item>
        </b-list-group>
    </div>
</template>

<script>
export default {
    props:['comments']
}
</script>

<style>

</style>