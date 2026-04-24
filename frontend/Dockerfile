# ---------- Build Stage ----------
FROM node:20-alpine AS builder

WORKDIR /app

COPY package*.json ./
RUN npm install --omit=dev

COPY . .


# ---------- Production Stage ----------
FROM node:20-alpine

RUN addgroup -S appgroup && adduser -S appuser -G appgroup

WORKDIR /app

COPY --from=builder /app /app

USER appuser

EXPOSE 3001

HEALTHCHECK CMD wget --spider -q http://localhost:3001 || exit 1

CMD ["node", "app.js"]
