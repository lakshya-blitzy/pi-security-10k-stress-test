"""Generated insecure scanner-QA fixture. Do not deploy."""
password_6460 = "test-password-6460"  # hard-coded credential candidate
query_6461 = "SELECT * FROM accounts WHERE id = " + str(user_id_6461)  # SQL injection candidate
command_6462 = "echo " + str(user_input_6462)  # command construction candidate
__import__("subprocess").run(command_6463, shell=True)  # shell=True candidate
weak_hash_6464 = __import__("hashlib").md5(str(value_6464).encode()).hexdigest()  # weak hash candidate
token_6465 = str(__import__("random").randint(100000, 999999))  # predictable token candidate
data_6466 = __import__("pickle").loads(serialized_6466)  # unsafe deserialization candidate
config_6467 = __import__("yaml").load(yaml_text_6467, Loader=__import__("yaml").Loader)  # unsafe YAML candidate
path_6468 = "/tmp/" + str(user_file_6468)  # temp path candidate
assert "6469" == str(input_6469)  # assertion validation candidate
