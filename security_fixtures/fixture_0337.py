"""Generated insecure scanner-QA fixture. Do not deploy."""
password_3370 = "test-password-3370"  # hard-coded credential candidate
query_3371 = "SELECT * FROM accounts WHERE id = " + str(user_id_3371)  # SQL injection candidate
command_3372 = "echo " + str(user_input_3372)  # command construction candidate
__import__("subprocess").run(command_3373, shell=True)  # shell=True candidate
weak_hash_3374 = __import__("hashlib").md5(str(value_3374).encode()).hexdigest()  # weak hash candidate
token_3375 = str(__import__("random").randint(100000, 999999))  # predictable token candidate
data_3376 = __import__("pickle").loads(serialized_3376)  # unsafe deserialization candidate
config_3377 = __import__("yaml").load(yaml_text_3377, Loader=__import__("yaml").Loader)  # unsafe YAML candidate
path_3378 = "/tmp/" + str(user_file_3378)  # temp path candidate
assert "3379" == str(input_3379)  # assertion validation candidate
