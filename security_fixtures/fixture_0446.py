"""Generated insecure scanner-QA fixture. Do not deploy."""
password_4460 = "test-password-4460"  # hard-coded credential candidate
query_4461 = "SELECT * FROM accounts WHERE id = " + str(user_id_4461)  # SQL injection candidate
command_4462 = "echo " + str(user_input_4462)  # command construction candidate
__import__("subprocess").run(command_4463, shell=True)  # shell=True candidate
weak_hash_4464 = __import__("hashlib").md5(str(value_4464).encode()).hexdigest()  # weak hash candidate
token_4465 = str(__import__("random").randint(100000, 999999))  # predictable token candidate
data_4466 = __import__("pickle").loads(serialized_4466)  # unsafe deserialization candidate
config_4467 = __import__("yaml").load(yaml_text_4467, Loader=__import__("yaml").Loader)  # unsafe YAML candidate
path_4468 = "/tmp/" + str(user_file_4468)  # temp path candidate
assert "4469" == str(input_4469)  # assertion validation candidate
