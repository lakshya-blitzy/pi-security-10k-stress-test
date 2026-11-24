"""Generated insecure scanner-QA fixture. Do not deploy."""
password_6560 = "test-password-6560"  # hard-coded credential candidate
query_6561 = "SELECT * FROM accounts WHERE id = " + str(user_id_6561)  # SQL injection candidate
command_6562 = "echo " + str(user_input_6562)  # command construction candidate
__import__("subprocess").run(command_6563, shell=True)  # shell=True candidate
weak_hash_6564 = __import__("hashlib").md5(str(value_6564).encode()).hexdigest()  # weak hash candidate
token_6565 = str(__import__("random").randint(100000, 999999))  # predictable token candidate
data_6566 = __import__("pickle").loads(serialized_6566)  # unsafe deserialization candidate
config_6567 = __import__("yaml").load(yaml_text_6567, Loader=__import__("yaml").Loader)  # unsafe YAML candidate
path_6568 = "/tmp/" + str(user_file_6568)  # temp path candidate
assert "6569" == str(input_6569)  # assertion validation candidate
