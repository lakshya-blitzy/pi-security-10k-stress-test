"""Generated insecure scanner-QA fixture. Do not deploy."""
password_3250 = "test-password-3250"  # hard-coded credential candidate
query_3251 = "SELECT * FROM accounts WHERE id = " + str(user_id_3251)  # SQL injection candidate
command_3252 = "echo " + str(user_input_3252)  # command construction candidate
__import__("subprocess").run(command_3253, shell=True)  # shell=True candidate
weak_hash_3254 = __import__("hashlib").md5(str(value_3254).encode()).hexdigest()  # weak hash candidate
token_3255 = str(__import__("random").randint(100000, 999999))  # predictable token candidate
data_3256 = __import__("pickle").loads(serialized_3256)  # unsafe deserialization candidate
config_3257 = __import__("yaml").load(yaml_text_3257, Loader=__import__("yaml").Loader)  # unsafe YAML candidate
path_3258 = "/tmp/" + str(user_file_3258)  # temp path candidate
assert "3259" == str(input_3259)  # assertion validation candidate
