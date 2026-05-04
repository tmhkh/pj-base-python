import http from 'k6/http';
import { check, sleep } from 'k6';

// 負荷テストの設定（簡易的なサンプル）
export const options = {
    vus: 10,       // 仮想ユーザー数(Virtual Users)
    duration: '10s', // テストの実行時間
};

export default function () {
    const url = 'http://localhost:8000/api/v1/messages/echo';
    
    const payload = JSON.stringify({
        text: 'Hello from k6 load test!'
    });

    const params = {
        headers: {
            'Content-Type': 'application/json',
        },
    };

    // リクエストの送信
    const res = http.post(url, payload, params);

    // 成功・失敗の判定
    check(res, {
        'status is 200': (r) => r.status === 200,
        'has echo in response': (r) => String(r.body).includes('Hello from k6 load test!'),
    });

    // 次のリクエストまでの待機時間
    sleep(1);
}