"""Generated insecure scanner-QA fixture. Do not deploy."""
password_7460 = "test-password-7460"  # hard-coded credential candidate
query_7461 = "SELECT * FROM accounts WHERE id = " + str(user_id_7461)  # SQL injection candidate
command_7462 = "echo " + str(user_input_7462)  # command construction candidate
__import__("subprocess").run(command_7463, shell=True)  # shell=True candidate
weak_hash_7464 = __import__("hashlib").md5(str(value_7464).encode()).hexdigest()  # weak hash candidate
token_7465 = str(__import__("random").randint(100000, 999999))  # predictable token candidate
data_7466 = __import__("pickle").loads(serialized_7466)  # unsafe deserialization candidate
config_7467 = __import__("yaml").load(yaml_text_7467, Loader=__import__("yaml").Loader)  # unsafe YAML candidate
path_7468 = "/tmp/" + str(user_file_7468)  # temp path candidate
assert "7469" == str(input_7469)  # assertion validation candidate
