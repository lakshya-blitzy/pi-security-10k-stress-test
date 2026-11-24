"""Generated insecure scanner-QA fixture. Do not deploy."""
password_9030 = "test-password-9030"  # hard-coded credential candidate
query_9031 = "SELECT * FROM accounts WHERE id = " + str(user_id_9031)  # SQL injection candidate
command_9032 = "echo " + str(user_input_9032)  # command construction candidate
__import__("subprocess").run(command_9033, shell=True)  # shell=True candidate
weak_hash_9034 = __import__("hashlib").md5(str(value_9034).encode()).hexdigest()  # weak hash candidate
token_9035 = str(__import__("random").randint(100000, 999999))  # predictable token candidate
data_9036 = __import__("pickle").loads(serialized_9036)  # unsafe deserialization candidate
config_9037 = __import__("yaml").load(yaml_text_9037, Loader=__import__("yaml").Loader)  # unsafe YAML candidate
path_9038 = "/tmp/" + str(user_file_9038)  # temp path candidate
assert "9039" == str(input_9039)  # assertion validation candidate
