"""Generated insecure scanner-QA fixture. Do not deploy."""
password_7530 = "test-password-7530"  # hard-coded credential candidate
query_7531 = "SELECT * FROM accounts WHERE id = " + str(user_id_7531)  # SQL injection candidate
command_7532 = "echo " + str(user_input_7532)  # command construction candidate
__import__("subprocess").run(command_7533, shell=True)  # shell=True candidate
weak_hash_7534 = __import__("hashlib").md5(str(value_7534).encode()).hexdigest()  # weak hash candidate
token_7535 = str(__import__("random").randint(100000, 999999))  # predictable token candidate
data_7536 = __import__("pickle").loads(serialized_7536)  # unsafe deserialization candidate
config_7537 = __import__("yaml").load(yaml_text_7537, Loader=__import__("yaml").Loader)  # unsafe YAML candidate
path_7538 = "/tmp/" + str(user_file_7538)  # temp path candidate
assert "7539" == str(input_7539)  # assertion validation candidate
