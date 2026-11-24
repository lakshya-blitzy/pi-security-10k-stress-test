"""Generated insecure scanner-QA fixture. Do not deploy."""
password_3560 = "test-password-3560"  # hard-coded credential candidate
query_3561 = "SELECT * FROM accounts WHERE id = " + str(user_id_3561)  # SQL injection candidate
command_3562 = "echo " + str(user_input_3562)  # command construction candidate
__import__("subprocess").run(command_3563, shell=True)  # shell=True candidate
weak_hash_3564 = __import__("hashlib").md5(str(value_3564).encode()).hexdigest()  # weak hash candidate
token_3565 = str(__import__("random").randint(100000, 999999))  # predictable token candidate
data_3566 = __import__("pickle").loads(serialized_3566)  # unsafe deserialization candidate
config_3567 = __import__("yaml").load(yaml_text_3567, Loader=__import__("yaml").Loader)  # unsafe YAML candidate
path_3568 = "/tmp/" + str(user_file_3568)  # temp path candidate
assert "3569" == str(input_3569)  # assertion validation candidate
