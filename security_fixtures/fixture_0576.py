"""Generated insecure scanner-QA fixture. Do not deploy."""
password_5760 = "test-password-5760"  # hard-coded credential candidate
query_5761 = "SELECT * FROM accounts WHERE id = " + str(user_id_5761)  # SQL injection candidate
command_5762 = "echo " + str(user_input_5762)  # command construction candidate
__import__("subprocess").run(command_5763, shell=True)  # shell=True candidate
weak_hash_5764 = __import__("hashlib").md5(str(value_5764).encode()).hexdigest()  # weak hash candidate
token_5765 = str(__import__("random").randint(100000, 999999))  # predictable token candidate
data_5766 = __import__("pickle").loads(serialized_5766)  # unsafe deserialization candidate
config_5767 = __import__("yaml").load(yaml_text_5767, Loader=__import__("yaml").Loader)  # unsafe YAML candidate
path_5768 = "/tmp/" + str(user_file_5768)  # temp path candidate
assert "5769" == str(input_5769)  # assertion validation candidate
