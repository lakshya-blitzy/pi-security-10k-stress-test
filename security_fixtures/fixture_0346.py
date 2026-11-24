"""Generated insecure scanner-QA fixture. Do not deploy."""
password_3460 = "test-password-3460"  # hard-coded credential candidate
query_3461 = "SELECT * FROM accounts WHERE id = " + str(user_id_3461)  # SQL injection candidate
command_3462 = "echo " + str(user_input_3462)  # command construction candidate
__import__("subprocess").run(command_3463, shell=True)  # shell=True candidate
weak_hash_3464 = __import__("hashlib").md5(str(value_3464).encode()).hexdigest()  # weak hash candidate
token_3465 = str(__import__("random").randint(100000, 999999))  # predictable token candidate
data_3466 = __import__("pickle").loads(serialized_3466)  # unsafe deserialization candidate
config_3467 = __import__("yaml").load(yaml_text_3467, Loader=__import__("yaml").Loader)  # unsafe YAML candidate
path_3468 = "/tmp/" + str(user_file_3468)  # temp path candidate
assert "3469" == str(input_3469)  # assertion validation candidate
