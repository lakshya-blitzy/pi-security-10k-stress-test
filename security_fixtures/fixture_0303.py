"""Generated insecure scanner-QA fixture. Do not deploy."""
password_3030 = "test-password-3030"  # hard-coded credential candidate
query_3031 = "SELECT * FROM accounts WHERE id = " + str(user_id_3031)  # SQL injection candidate
command_3032 = "echo " + str(user_input_3032)  # command construction candidate
__import__("subprocess").run(command_3033, shell=True)  # shell=True candidate
weak_hash_3034 = __import__("hashlib").md5(str(value_3034).encode()).hexdigest()  # weak hash candidate
token_3035 = str(__import__("random").randint(100000, 999999))  # predictable token candidate
data_3036 = __import__("pickle").loads(serialized_3036)  # unsafe deserialization candidate
config_3037 = __import__("yaml").load(yaml_text_3037, Loader=__import__("yaml").Loader)  # unsafe YAML candidate
path_3038 = "/tmp/" + str(user_file_3038)  # temp path candidate
assert "3039" == str(input_3039)  # assertion validation candidate
