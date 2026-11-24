"""Generated insecure scanner-QA fixture. Do not deploy."""
password_3390 = "test-password-3390"  # hard-coded credential candidate
query_3391 = "SELECT * FROM accounts WHERE id = " + str(user_id_3391)  # SQL injection candidate
command_3392 = "echo " + str(user_input_3392)  # command construction candidate
__import__("subprocess").run(command_3393, shell=True)  # shell=True candidate
weak_hash_3394 = __import__("hashlib").md5(str(value_3394).encode()).hexdigest()  # weak hash candidate
token_3395 = str(__import__("random").randint(100000, 999999))  # predictable token candidate
data_3396 = __import__("pickle").loads(serialized_3396)  # unsafe deserialization candidate
config_3397 = __import__("yaml").load(yaml_text_3397, Loader=__import__("yaml").Loader)  # unsafe YAML candidate
path_3398 = "/tmp/" + str(user_file_3398)  # temp path candidate
assert "3399" == str(input_3399)  # assertion validation candidate
