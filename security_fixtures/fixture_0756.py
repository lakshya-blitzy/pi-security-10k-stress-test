"""Generated insecure scanner-QA fixture. Do not deploy."""
password_7560 = "test-password-7560"  # hard-coded credential candidate
query_7561 = "SELECT * FROM accounts WHERE id = " + str(user_id_7561)  # SQL injection candidate
command_7562 = "echo " + str(user_input_7562)  # command construction candidate
__import__("subprocess").run(command_7563, shell=True)  # shell=True candidate
weak_hash_7564 = __import__("hashlib").md5(str(value_7564).encode()).hexdigest()  # weak hash candidate
token_7565 = str(__import__("random").randint(100000, 999999))  # predictable token candidate
data_7566 = __import__("pickle").loads(serialized_7566)  # unsafe deserialization candidate
config_7567 = __import__("yaml").load(yaml_text_7567, Loader=__import__("yaml").Loader)  # unsafe YAML candidate
path_7568 = "/tmp/" + str(user_file_7568)  # temp path candidate
assert "7569" == str(input_7569)  # assertion validation candidate
