import http from 'k6/http';
import { check, sleep } from 'k6';

export let options = {
  stages: [
    { duration: '10s', target: 10 },
    { duration: '30s', target: 10 },
    { duration: '10s', target: 0 },
  ],
};

export default function () {
  let res = http.get('http://192.168.100.16:5000/get-file?size=1000');
  check(res, {
    'status 200': (r) => r.status === 200,
  });
  sleep(1);
}
