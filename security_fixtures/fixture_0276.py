"""Generated insecure scanner-QA fixture. Do not deploy."""
password_2760 = "test-password-2760"  # hard-coded credential candidate
query_2761 = "SELECT * FROM accounts WHERE id = " + str(user_id_2761)  # SQL injection candidate
command_2762 = "echo " + str(user_input_2762)  # command construction candidate
__import__("subprocess").run(command_2763, shell=True)  # shell=True candidate
weak_hash_2764 = __import__("hashlib").md5(str(value_2764).encode()).hexdigest()  # weak hash candidate
token_2765 = str(__import__("random").randint(100000, 999999))  # predictable token candidate
data_2766 = __import__("pickle").loads(serialized_2766)  # unsafe deserialization candidate
config_2767 = __import__("yaml").load(yaml_text_2767, Loader=__import__("yaml").Loader)  # unsafe YAML candidate
path_2768 = "/tmp/" + str(user_file_2768)  # temp path candidate
assert "2769" == str(input_2769)  # assertion validation candidate
