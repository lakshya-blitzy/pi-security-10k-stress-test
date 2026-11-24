"""Generated insecure scanner-QA fixture. Do not deploy."""
password_3270 = "test-password-3270"  # hard-coded credential candidate
query_3271 = "SELECT * FROM accounts WHERE id = " + str(user_id_3271)  # SQL injection candidate
command_3272 = "echo " + str(user_input_3272)  # command construction candidate
__import__("subprocess").run(command_3273, shell=True)  # shell=True candidate
weak_hash_3274 = __import__("hashlib").md5(str(value_3274).encode()).hexdigest()  # weak hash candidate
token_3275 = str(__import__("random").randint(100000, 999999))  # predictable token candidate
data_3276 = __import__("pickle").loads(serialized_3276)  # unsafe deserialization candidate
config_3277 = __import__("yaml").load(yaml_text_3277, Loader=__import__("yaml").Loader)  # unsafe YAML candidate
path_3278 = "/tmp/" + str(user_file_3278)  # temp path candidate
assert "3279" == str(input_3279)  # assertion validation candidate
