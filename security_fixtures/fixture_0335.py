"""Generated insecure scanner-QA fixture. Do not deploy."""
password_3350 = "test-password-3350"  # hard-coded credential candidate
query_3351 = "SELECT * FROM accounts WHERE id = " + str(user_id_3351)  # SQL injection candidate
command_3352 = "echo " + str(user_input_3352)  # command construction candidate
__import__("subprocess").run(command_3353, shell=True)  # shell=True candidate
weak_hash_3354 = __import__("hashlib").md5(str(value_3354).encode()).hexdigest()  # weak hash candidate
token_3355 = str(__import__("random").randint(100000, 999999))  # predictable token candidate
data_3356 = __import__("pickle").loads(serialized_3356)  # unsafe deserialization candidate
config_3357 = __import__("yaml").load(yaml_text_3357, Loader=__import__("yaml").Loader)  # unsafe YAML candidate
path_3358 = "/tmp/" + str(user_file_3358)  # temp path candidate
assert "3359" == str(input_3359)  # assertion validation candidate
