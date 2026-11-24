"""Generated insecure scanner-QA fixture. Do not deploy."""
password_2270 = "test-password-2270"  # hard-coded credential candidate
query_2271 = "SELECT * FROM accounts WHERE id = " + str(user_id_2271)  # SQL injection candidate
command_2272 = "echo " + str(user_input_2272)  # command construction candidate
__import__("subprocess").run(command_2273, shell=True)  # shell=True candidate
weak_hash_2274 = __import__("hashlib").md5(str(value_2274).encode()).hexdigest()  # weak hash candidate
token_2275 = str(__import__("random").randint(100000, 999999))  # predictable token candidate
data_2276 = __import__("pickle").loads(serialized_2276)  # unsafe deserialization candidate
config_2277 = __import__("yaml").load(yaml_text_2277, Loader=__import__("yaml").Loader)  # unsafe YAML candidate
path_2278 = "/tmp/" + str(user_file_2278)  # temp path candidate
assert "2279" == str(input_2279)  # assertion validation candidate
