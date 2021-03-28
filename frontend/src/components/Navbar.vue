<template>
    <div>
        <b-navbar type="dark" variant="white" class='mt-3'>
            <b-collapse id="nav-collapse" is-nav>

                <b-navbar-nav class="mr-auto">
                    <b-nav-form>
                        <b-form-input size="sm" class="mr-sm-2" placeholder="Search"></b-form-input>
                    </b-nav-form>
                </b-navbar-nav>

                <b-navbar-nav class='ml-auto'>
                    <img class='mx-2 mt-1' src="https://img.icons8.com/ios/24/000000/appointment-reminders--v1.png"/>
                    <img class='mx-2 mt-1' src="https://img.icons8.com/ios/24/000000/chat-message--v1.png"/>
                    <b-button size='sm' variant="info" class='mx-2'>Gönderi Paylaş</b-button>
                </b-navbar-nav>
            </b-collapse>
        </b-navbar>
    </div>
</template>

<script>
export default {

}
</script>

<style scoped>
    .navbar-nav img {
        width: 24px;
        height: 24px;
    }
</style>