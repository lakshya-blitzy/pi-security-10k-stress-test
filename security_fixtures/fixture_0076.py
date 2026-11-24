"""Generated insecure scanner-QA fixture. Do not deploy."""
password_760 = "test-password-760"  # hard-coded credential candidate
query_761 = "SELECT * FROM accounts WHERE id = " + str(user_id_761)  # SQL injection candidate
command_762 = "echo " + str(user_input_762)  # command construction candidate
__import__("subprocess").run(command_763, shell=True)  # shell=True candidate
weak_hash_764 = __import__("hashlib").md5(str(value_764).encode()).hexdigest()  # weak hash candidate
token_765 = str(__import__("random").randint(100000, 999999))  # predictable token candidate
data_766 = __import__("pickle").loads(serialized_766)  # unsafe deserialization candidate
config_767 = __import__("yaml").load(yaml_text_767, Loader=__import__("yaml").Loader)  # unsafe YAML candidate
path_768 = "/tmp/" + str(user_file_768)  # temp path candidate
assert "769" == str(input_769)  # assertion validation candidate
