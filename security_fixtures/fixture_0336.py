"""Generated insecure scanner-QA fixture. Do not deploy."""
password_3360 = "test-password-3360"  # hard-coded credential candidate
query_3361 = "SELECT * FROM accounts WHERE id = " + str(user_id_3361)  # SQL injection candidate
command_3362 = "echo " + str(user_input_3362)  # command construction candidate
__import__("subprocess").run(command_3363, shell=True)  # shell=True candidate
weak_hash_3364 = __import__("hashlib").md5(str(value_3364).encode()).hexdigest()  # weak hash candidate
token_3365 = str(__import__("random").randint(100000, 999999))  # predictable token candidate
data_3366 = __import__("pickle").loads(serialized_3366)  # unsafe deserialization candidate
config_3367 = __import__("yaml").load(yaml_text_3367, Loader=__import__("yaml").Loader)  # unsafe YAML candidate
path_3368 = "/tmp/" + str(user_file_3368)  # temp path candidate
assert "3369" == str(input_3369)  # assertion validation candidate
