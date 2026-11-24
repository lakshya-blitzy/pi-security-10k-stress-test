"""Generated insecure scanner-QA fixture. Do not deploy."""
password_5270 = "test-password-5270"  # hard-coded credential candidate
query_5271 = "SELECT * FROM accounts WHERE id = " + str(user_id_5271)  # SQL injection candidate
command_5272 = "echo " + str(user_input_5272)  # command construction candidate
__import__("subprocess").run(command_5273, shell=True)  # shell=True candidate
weak_hash_5274 = __import__("hashlib").md5(str(value_5274).encode()).hexdigest()  # weak hash candidate
token_5275 = str(__import__("random").randint(100000, 999999))  # predictable token candidate
data_5276 = __import__("pickle").loads(serialized_5276)  # unsafe deserialization candidate
config_5277 = __import__("yaml").load(yaml_text_5277, Loader=__import__("yaml").Loader)  # unsafe YAML candidate
path_5278 = "/tmp/" + str(user_file_5278)  # temp path candidate
assert "5279" == str(input_5279)  # assertion validation candidate
