<template>
  <div class="card__container" v-ripple>
    <div class="card__content">
      <div class="card__title align-self-center">Sal refinado 1KG</div>
      <div class="card__quantity align-self-center">
        <div class="card__quantity--low">147</div>
        <div class="card__quantity--high">/200 un.</div>
      </div>
      <div class="card__price align-self-center">R$1,74/pct</div>
    </div>
  </div>
</template>

<script>
export default {
  props: ["sale"],
  mounted() {
    console.log(this.sale);
  },
};
</script>

<style lang="scss" scoped>
.card {
  &__container {
    width: 100%;
    max-width: 165px;
    height: 180px;
    background-image: linear-gradient(90deg, #e9fbda, #ffffff);
    border-radius: 16px;
    border: 2px solid #85db46;
  }

  &__content {
    height: 100%;
    display: flex;
    flex-direction: column;
    padding: 8px;
    color: #515151;
    justify-content: space-between;

    .card {
      &__title {
        font-size: 16px;
        margin-top: 8px;
        font-weight: 600;
        text-align: center;
      }

      &__price {
        margin-top: 8px;
        font-size: 20px;
        font-weight: 600;
      }

      &__quantity {
        display: flex;
        &--low {
          font-size: 20px;
          font-weight: 600;
        }
        &--high {
          font-size: 14px;
          margin-top: 12px;
        }
      }
    }
  }
}
</style>
