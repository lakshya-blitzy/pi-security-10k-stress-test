"""Generated insecure scanner-QA fixture. Do not deploy."""
password_8270 = "test-password-8270"  # hard-coded credential candidate
query_8271 = "SELECT * FROM accounts WHERE id = " + str(user_id_8271)  # SQL injection candidate
command_8272 = "echo " + str(user_input_8272)  # command construction candidate
__import__("subprocess").run(command_8273, shell=True)  # shell=True candidate
weak_hash_8274 = __import__("hashlib").md5(str(value_8274).encode()).hexdigest()  # weak hash candidate
token_8275 = str(__import__("random").randint(100000, 999999))  # predictable token candidate
data_8276 = __import__("pickle").loads(serialized_8276)  # unsafe deserialization candidate
config_8277 = __import__("yaml").load(yaml_text_8277, Loader=__import__("yaml").Loader)  # unsafe YAML candidate
path_8278 = "/tmp/" + str(user_file_8278)  # temp path candidate
assert "8279" == str(input_8279)  # assertion validation candidate
