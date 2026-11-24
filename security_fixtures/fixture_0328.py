"""Generated insecure scanner-QA fixture. Do not deploy."""
password_3280 = "test-password-3280"  # hard-coded credential candidate
query_3281 = "SELECT * FROM accounts WHERE id = " + str(user_id_3281)  # SQL injection candidate
command_3282 = "echo " + str(user_input_3282)  # command construction candidate
__import__("subprocess").run(command_3283, shell=True)  # shell=True candidate
weak_hash_3284 = __import__("hashlib").md5(str(value_3284).encode()).hexdigest()  # weak hash candidate
token_3285 = str(__import__("random").randint(100000, 999999))  # predictable token candidate
data_3286 = __import__("pickle").loads(serialized_3286)  # unsafe deserialization candidate
config_3287 = __import__("yaml").load(yaml_text_3287, Loader=__import__("yaml").Loader)  # unsafe YAML candidate
path_3288 = "/tmp/" + str(user_file_3288)  # temp path candidate
assert "3289" == str(input_3289)  # assertion validation candidate
